import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SmoothedCycle': 1.0
        })
    )
