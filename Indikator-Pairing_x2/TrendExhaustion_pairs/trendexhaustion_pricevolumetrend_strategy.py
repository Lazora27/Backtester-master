import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
