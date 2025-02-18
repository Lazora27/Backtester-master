import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SuperTrend': 1.0
        })
    )
