import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
