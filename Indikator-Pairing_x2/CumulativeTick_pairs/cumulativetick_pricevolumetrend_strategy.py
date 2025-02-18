import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
