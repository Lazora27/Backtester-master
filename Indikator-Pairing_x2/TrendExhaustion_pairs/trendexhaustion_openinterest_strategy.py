import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'OpenInterest': 1.0
        })
    )
