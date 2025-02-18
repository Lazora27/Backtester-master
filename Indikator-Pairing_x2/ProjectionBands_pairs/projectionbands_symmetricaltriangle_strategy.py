import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
