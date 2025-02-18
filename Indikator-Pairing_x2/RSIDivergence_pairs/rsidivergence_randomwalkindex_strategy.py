import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
