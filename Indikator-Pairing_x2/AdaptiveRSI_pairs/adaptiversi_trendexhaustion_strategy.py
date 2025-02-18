import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TrendExhaustion': 1.0
        })
    )
