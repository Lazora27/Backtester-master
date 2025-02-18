import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
