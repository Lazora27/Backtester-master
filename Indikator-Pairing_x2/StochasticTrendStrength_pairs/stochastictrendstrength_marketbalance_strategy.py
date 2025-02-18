import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MarketBalance': 1.0
        })
    )
