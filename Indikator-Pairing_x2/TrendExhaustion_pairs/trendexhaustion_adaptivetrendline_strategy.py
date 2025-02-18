import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
