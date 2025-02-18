import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
