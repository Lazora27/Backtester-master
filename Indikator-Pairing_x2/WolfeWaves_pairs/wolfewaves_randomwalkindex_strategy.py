import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
