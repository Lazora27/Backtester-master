import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
