import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BuyingPressure': 1.0
        })
    )
