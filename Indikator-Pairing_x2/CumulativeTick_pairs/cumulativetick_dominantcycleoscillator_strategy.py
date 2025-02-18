import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
