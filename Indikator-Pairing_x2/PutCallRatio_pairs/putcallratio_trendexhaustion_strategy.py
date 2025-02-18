import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TrendExhaustion': 1.0
        })
    )
