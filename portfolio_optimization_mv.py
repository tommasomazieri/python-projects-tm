"""
Hello,
this is a portfolio optimization script, following single-index model, mean-variance portfolio optimization.

documentations regarding this script can be found in 'portfolio_optimization_script_docs' folder

!!!WARNING!!!
Please note that, for the currency conversion, to get investor's currency values of international stocks, we use a func
which is backed by a financial data provider API, so how you personally do to get converted values is up to you, but,
is important that the inputs and the outputs of given function are as described in the sample function I provided below
(currency_conversion_dataframe)


As of now, the code by itself (so excluding all the data gathering process) takes around 8 seconds to provide its output
It might be sped up in the future, although, being of no real practical use, I think that without external demand, I
wont keep working on it any longer
"""
import string
import timeit
import json

import numpy as np
from arch import arch_model
import pandas as pd
from scipy.stats import stats
from scipy import optimize as sco
import pyarrow  # to read parquet files

pd.options.display.float_format = "{:,.9f}".format
pd.set_option('display.max_columns', 34)


def currency_conversion_dataframe(dataframe) -> pd.DataFrame:
    """
    :param dataframe: assets_prices[['pairs', 'amount']]
        where pairs is: price_currency/investor_currency; amount is price currency prices
        Note that you also get investor_currency/investor_currency if price currency is also investor currency
    """
    for i, row in dataframe.iterrows():
        cur = row[0].split("/")
        if cur[0] != cur[1]:  # you will check for different currencies in pairs...
            # here, row[0] is the pair (i.e. USD/EUR) and the amount is row[1] (i.e. 74.1)
            def currency_conversion(r1, amt=1):
                return 0
            conv = currency_conversion(row[0], amt=row[1])  # ... and apply curr_conversion func of your choice
            dataframe.loc[i, 'amount'] = float(conv['amount'])  # replace here value of foreign denominated prices
    return dataframe


def compute_egarch_variance(returns: pd.DataFrame, distribution_of_returns: str = 'normal', n_simulations=200, rescale=False) -> float:
    eam = arch_model(
        returns, p=1, q=1, o=1, mean='constant', power=2.0, vol='EGARCH', dist=distribution_of_returns, rescale=rescale
    )
    eam_fit = eam.fit(disp='off')
    forecast_average_variance = eam_fit.forecast(
        horizon=252, method="simulation", simulations=n_simulations, reindex=False
    ).variance.T.mean() * 252
    return (forecast_average_variance / 10_000).values[0]


class InternationalDiversification:  # v: 1.0.0
    """we need to revisit the code theory for that one, also for his integration to efficient frontier script"""
    # WE SET CURRENCIES RETURNS TO 0, SO ONLY VARIANCES ARE TAKEN INTO ACCOUNT
    def __init__(
            self,
            portfolio: pd.DataFrame,
            risk_free_rate: float,
            returns_dataframe: pd.DataFrame,
            currencies_returns_to_base: pd.DataFrame,
            quote_currency="EUR"
    ):
        self.qc = quote_currency
        self.rf_rate = risk_free_rate
        self.pf = portfolio.set_index('stock_id')
        self.returns_dataframe = returns_dataframe
        self.curr_df = currencies_returns_to_base

    def variances(self) -> pd.DataFrame:
        """return the dataframe with symbol variance, his currency variance and the covariance between symbol and
        currency"""
        for column in self.returns_dataframe.columns:
            currency = column.split("_")[-1]
            if currency != self.qc:
                fx = f'{currency}/{self.qc}'
                ret_product = self.returns_dataframe[column] * self.curr_df[fx]
                self.returns_dataframe[column] = self.returns_dataframe[column] + self.curr_df[fx] + ret_product

        self.pf['sigma_2'] = 0
        for asset in self.returns_dataframe:
            asset_return = self.returns_dataframe[asset].dropna() * 100
            self.pf.loc[asset, 'sigma_2'] = compute_egarch_variance(returns=asset_return, n_simulations=200)
        return self.pf


# for the shorting part, change to standard method (sum weights == 1) from the Lintner method (sum abs(w) == 1)
class EfficientFrontier:  # v: 1.0.0
    """at first define the rules: short=True, rf_rate_debt=True. You can choose which one is true, and based on that,
    an efficient frontier will be formed with the asset list provided. it only works for stocks right now, but it could
    implement other asset classes (the firs should be ETFs). the stock list should provide:
    [(symbol, exchange), (...), ...]
    This execution is quite slow just with 9 assets. We need to speed it up!

    REWRITE HERE THE NEW DESCRIPTION OF THE CLASS: WHAT DOES IT DO, HOW DOES IT DO IT
    """

    def __init__(
            self,
            selected_assets: pd.DataFrame,
            assets_returns: pd.DataFrame,
            assets_prices: pd.DataFrame,
            benchmark_market_data: pd.DataFrame,
            benchmark_market_returns: pd.DataFrame,
            currencies_returns_to_base: pd.DataFrame,
            risk_free_rate: float,
            invested_capital: float | int = 100_000,
            short=False,  # for now, no short positions are allowed
            bound_lim=(0, 1),
            portfolio_currency: str = "EUR"
            # add currencies returns to be passed to process_input_data() !!!
    ):
        self.invested_capital = invested_capital
        self.currency = portfolio_currency

        self.portfolio = selected_assets  # see table format in docs. You should add an alpha column to sum to CAPM val.
        self.assets_returns = assets_returns  # see table format in docs
        self.assets_prices = assets_prices  # see table format in docs

        self.mdf = benchmark_market_data  # see table format in docs
        self.mkt_name, self.mkt_implied_return = self.mdf['symbol'].values[0], self.mdf['implied_return'].values[0]
        self.mkt_returns = benchmark_market_returns.dropna() * 100
        self.market_variance = compute_egarch_variance(returns=self.mkt_returns, n_simulations=200)

        self.rf_rate = risk_free_rate  # value expressed in decimals, not percentage

        self.processed_data = self.process_input_data(currencies_returns_to_base)

        self.bound = bound_lim if short is False else (-1, 1)

    def portfolio_performance(self, weights) -> (float, float):
        """a way to improve that part, for each portfolio provided, is to take the expected returns from a CAPM or APT
        model as the portfolio_return"""
        df = self.processed_data  # to make next lines of code shorter...
        df["weights"] = weights.astype('float64')
        portfolio_return = np.sum(df["implied_return"] * df["weights"])  # annualized pf returns...
        sigma_e_pf = sum(df["weights"] ** 2 * df["sigma_e"])  # add it later to dataframe...
        annual_var = (sum(df["weights"] * df['beta']) ** 2) * self.market_variance + sigma_e_pf
        portfolio_risk = np.sqrt(annual_var)
        return portfolio_return, portfolio_risk

    def portfolio_variance(self, weights) -> float:
        return self.portfolio_performance(weights)[1]

    def portfolio_returns(self, weights) -> float:
        return self.portfolio_performance(weights)[0]

    def minimum_variance(self):
        n_assets = len(self.portfolio)
        constraints = ({"type": "eq", "fun": lambda x: np.sum(abs(x)) - 1})
        bounds = tuple(self.bound for x in range(n_assets))
        var = sco.minimize(self.portfolio_variance, np.array(n_assets * [1. / n_assets]), method="SLSQP", bounds=bounds,
                           constraints=constraints)
        return var.fun, var.x

    def efficient_optimization(self, return_target):
        """for each return target, we optimize the portfolio for min_variance"""
        n_assets = len(self.portfolio)
        constraints = ({"type": "eq", "fun": lambda x: self.portfolio_returns(x) - return_target},  # pf ret == ret trg
                       {"type": "eq", "fun": lambda x: np.sum(abs(x)) - 1})  # sum of weights == 1
        bounds = tuple(self.bound for _ in range(n_assets))
        opt = sco.minimize(self.portfolio_variance, np.array(n_assets * [1. / n_assets]), method="SLSQP", bounds=bounds,
                           constraints=constraints)
        return opt.fun, opt.x

    def process_input_data(self, currencies_returns_to_base) -> pd.DataFrame:
        # to make it more understandable, maybe we should substitute df0 with self.portfolio...
        df0 = InternationalDiversification(
            portfolio=self.portfolio,
            risk_free_rate=self.rf_rate,
            quote_currency=self.currency,
            returns_dataframe=self.assets_returns,
            currencies_returns_to_base=currencies_returns_to_base
        ).variances()
        # DESCRIBE WHAT YOU ARE DOING HERE. REMOVE USELESS STEPS...
        # STARTS MEASURING CAPM RETURNS OF EACH ASSET:
        df0['implied_return'] = (self.mkt_implied_return-self.rf_rate)*df0["beta"] + self.rf_rate + df0['alphas']
        # NOW COMPUTES VARIANCES OF EACH ASSET:
        df0["excess_ret"] = df0['implied_return'] - self.rf_rate
        df0["excess_ret_beta"] = df0["excess_ret"] / df0["beta"]

        df0 = df0.sort_values(by=["excess_ret_beta"], axis=0, ascending=False)
        # we measure sigma_e here. We use variances from intern_diver
        df0["sigma_e"] = abs(df0["sigma_2"] - self.market_variance * df0["beta"] ** 2)  # CHECK IT!
        df0["exc_beta_sigma_e"] = df0["excess_ret"] * df0["beta"] / df0["sigma_e"]
        df0["beta_sigma_e"] = df0["beta"] ** 2 / df0["sigma_e"]

        df0 = df0.reset_index()
        df0["sum_exc_b_s"] = [df0["exc_beta_sigma_e"].iloc[0:i + 1].sum() for i, row in df0.iterrows()]
        df0["sum_beta_sigma"] = [df0["beta_sigma_e"].iloc[0:i + 1].sum() for i, row in df0.iterrows()]
        df0["C_i"] = (df0["sum_exc_b_s"] * self.market_variance) / (1 + self.market_variance * df0["sum_beta_sigma"])
        return df0

    def measure_c_value(self) -> (pd.DataFrame, float):
        df = self.processed_data
        # speed it up!
        df["acceptable"] = [
            df["excess_ret_beta"][i + 1] - df["C_i"][i] if (i + 1 <= len(df) - 1) else 0 for i, row in df.iterrows()
        ]
        in_portfolio = df[df.acceptable > 0]
        # return in_portfolio.drop("acceptable", axis=1)
        c_best = in_portfolio["C_i"].to_numpy()[-1]
        return df, c_best

    def optimal_portfolio_calculator(self) -> np.array:
        df, c_best = self.measure_c_value()
        df["zetas"] = (df['beta'] / df["sigma_e"]) * (df["excess_ret_beta"] - c_best)
        df.loc[df['acceptable'] <= 0, 'zetas'] = 0
        df["weights"] = df["zetas"] / df["zetas"].sum()
        # return df.drop("acceptable", axis=1)
        return df["weights"].to_numpy()

    def efficient_frontier(self) -> (pd.DataFrame, pd.DataFrame):
        target_returns = np.linspace(
            self.portfolio_performance(self.minimum_variance()[1])[0],
            self.portfolio_performance(self.optimal_portfolio_calculator())[0],
            10
        )

        # TRY TO SPEED IT UP IN FUTURE UPDATES:
        tgt_rets = len(target_returns)
        weights_list = np.zeros(shape=(tgt_rets, len(self.portfolio)))
        # make just one list called eff_front and index better in for loop...
        volatilities = np.zeros(tgt_rets)
        sharpe_ratio = np.zeros(tgt_rets)
        sigma_e = np.zeros(tgt_rets)
        # see how to make all this code shorter...
        portfolios = list(string.ascii_uppercase)[:len(target_returns)]
        self.processed_data = self.processed_data.set_index('stock_id')
        sigma_e_base = self.processed_data["sigma_e"].T
        i = 0
        for target in target_returns:
            volatility, weights = self.efficient_optimization(target)
            weights_list[i] = weights
            volatilities[i] = volatility
            sharpe_ratio[i] = (target - self.rf_rate) / volatility
            sigma_e[i] = sum((weights ** 2) * sigma_e_base) ** .5
            i += 1

        efficient_frontier = pd.DataFrame(
            np.array([target_returns, volatilities, sharpe_ratio, sigma_e]).transpose(),
            index=portfolios,
            columns=["returns", "volatility", "s_ratio", 'sigma_e']
        )
        weightings = pd.DataFrame(
            np.array(weights_list), index=portfolios, columns=self.processed_data.index
        )
        # we might make a function that measures the diversification of a portfolio so that can be generically used
        return efficient_frontier, weightings

    def portfolio_allocation(self, currency_conversion_function) -> (json, json):
        """define the allocation of your capital to the various selected assets, given their current prices and weights
        provided. It will return the stock allocation (n. of shares) and the value (in the chosen currency).
        """
        eff_fr, weightings = self.efficient_frontier()

        self.assets_prices['pairs'] = self.assets_prices['currency'] + '/' + self.currency
        self.assets_prices['amount'] = self.assets_prices['close'].astype('float64')
        # THIS FUNCTION NEED API... NOT GOOD NOW BRUH...
        prices = currency_conversion_function(self.assets_prices[['pairs', 'amount']])["amount"]
        shares = (weightings * self.invested_capital) // prices.T  # make sure prices and weights are matched...

        pf_value = (shares * prices.T).sum(axis=1)
        print('effective capital invested: ')
        print(pf_value)

        portfolios_dataframe = pd.concat([eff_fr, shares], axis=1)
        weightings_dataframe = pd.concat([eff_fr, weightings], axis=1)
        portfolios_dataframe["prob_neg_returns"] = 1 - stats.norm.sf(-portfolios_dataframe["returns"] / portfolios_dataframe["volatility"])
        weightings_dataframe["prob_neg_returns"] = portfolios_dataframe["prob_neg_returns"]

        print(portfolios_dataframe)
        # make localizations files to have it run in different languages!
        pf_choice = input(f'inserire la lettera del portafoglio che desidera selezionare: ')
        portfolio_shares = portfolios_dataframe.loc[pf_choice].to_json()
        portfolio_weightings = weightings_dataframe.loc[pf_choice].to_json()
        return portfolio_shares, portfolio_weightings


if __name__ == "__main__":
    start = timeit.default_timer()

    # LOAD ALL INPUTS FROM EXTERNAL SAMPLE PARQUET FILES
    assets_data = pd.read_parquet('assets_data.parquet')  # change asset data: get only the beta of market of choice!
    assets_daily_returns = pd.read_parquet('assets_daily_returns.parquet')
    assets_prices = pd.read_parquet('assets_prices.parquet')
    benchmark_market_data = pd.read_parquet('benchmark_market_data.parquet')
    print(benchmark_market_data)
    benchmark_market_daily_returns = pd.read_parquet('benchmark_market_daily_returns.parquet')
    currencies_returns_to_base = pd.read_parquet('currencies_returns_to_base.parquet')
    rf = .034

    print(
        EfficientFrontier(
            assets_data, assets_daily_returns, assets_prices, benchmark_market_data, benchmark_market_daily_returns,
            currencies_returns_to_base, rf, invested_capital=100_000, bound_lim=(0, 1), portfolio_currency="EUR"
        ).portfolio_allocation(currency_conversion_function=currency_conversion_dataframe)
    )

    stop = timeit.default_timer()
    print("tempo esecuzione: " + str(stop - start) + ' secondi')
