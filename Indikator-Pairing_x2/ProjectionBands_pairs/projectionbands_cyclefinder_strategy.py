import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'CycleFinder': 1.0
        })
    )
