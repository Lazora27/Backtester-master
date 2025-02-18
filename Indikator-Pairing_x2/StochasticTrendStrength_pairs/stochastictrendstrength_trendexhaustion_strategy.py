import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TrendExhaustion': 1.0
        })
    )
