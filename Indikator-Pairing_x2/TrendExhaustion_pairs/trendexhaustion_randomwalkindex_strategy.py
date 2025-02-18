import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
