import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CumulativeTick': 1.0
        })
    )
