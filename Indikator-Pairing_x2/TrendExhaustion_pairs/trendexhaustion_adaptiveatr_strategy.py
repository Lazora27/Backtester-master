import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AdaptiveATR': 1.0
        })
    )
