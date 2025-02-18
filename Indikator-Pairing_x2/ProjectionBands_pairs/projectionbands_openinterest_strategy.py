import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'OpenInterest': 1.0
        })
    )
