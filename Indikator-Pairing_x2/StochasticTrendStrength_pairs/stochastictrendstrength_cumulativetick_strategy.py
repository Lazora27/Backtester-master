import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CumulativeTick': 1.0
        })
    )
