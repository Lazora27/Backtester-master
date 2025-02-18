import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
