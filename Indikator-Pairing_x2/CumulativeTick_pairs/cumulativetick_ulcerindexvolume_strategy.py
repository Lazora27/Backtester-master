import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
