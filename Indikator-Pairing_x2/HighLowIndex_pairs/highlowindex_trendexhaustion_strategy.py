import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
