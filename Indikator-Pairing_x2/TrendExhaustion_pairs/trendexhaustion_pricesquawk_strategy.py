import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PriceSquawk': 1.0
        })
    )
