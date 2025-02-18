import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ExtensionProjections': 1.0
        })
    )
