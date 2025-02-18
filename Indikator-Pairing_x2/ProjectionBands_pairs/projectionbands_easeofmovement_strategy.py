import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'EaseOfMovement': 1.0
        })
    )
