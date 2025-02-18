import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und GannAngles
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'GannAngles': 1.0
        })
    )
