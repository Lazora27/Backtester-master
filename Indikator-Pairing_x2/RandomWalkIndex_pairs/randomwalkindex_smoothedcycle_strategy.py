import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
