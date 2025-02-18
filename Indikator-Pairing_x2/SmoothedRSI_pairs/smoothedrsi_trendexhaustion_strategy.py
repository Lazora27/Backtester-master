import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TrendExhaustion': 1.0
        })
    )
