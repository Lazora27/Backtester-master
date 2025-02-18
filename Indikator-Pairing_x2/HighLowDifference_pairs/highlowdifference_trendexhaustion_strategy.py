import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TrendExhaustion': 1.0
        })
    )
