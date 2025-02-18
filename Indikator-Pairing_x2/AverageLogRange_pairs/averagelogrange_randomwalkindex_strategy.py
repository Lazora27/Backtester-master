import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
