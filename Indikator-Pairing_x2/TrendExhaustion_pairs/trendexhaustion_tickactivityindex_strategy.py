import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TickActivityIndex': 1.0
        })
    )
