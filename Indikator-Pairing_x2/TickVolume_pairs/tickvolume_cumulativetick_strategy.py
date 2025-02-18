import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CumulativeTick': 1.0
        })
    )
