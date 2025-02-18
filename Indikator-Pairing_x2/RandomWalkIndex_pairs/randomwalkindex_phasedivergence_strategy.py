import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
