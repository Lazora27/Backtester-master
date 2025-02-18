import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
