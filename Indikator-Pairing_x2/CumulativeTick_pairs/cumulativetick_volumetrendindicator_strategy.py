import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
