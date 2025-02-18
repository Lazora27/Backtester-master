import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
