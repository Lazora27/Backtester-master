import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
