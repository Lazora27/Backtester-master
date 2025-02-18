import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
