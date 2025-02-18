import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
