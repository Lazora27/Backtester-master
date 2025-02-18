import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
