import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
