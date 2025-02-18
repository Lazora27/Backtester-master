import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
