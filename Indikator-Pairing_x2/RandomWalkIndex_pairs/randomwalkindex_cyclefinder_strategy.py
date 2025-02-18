import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
