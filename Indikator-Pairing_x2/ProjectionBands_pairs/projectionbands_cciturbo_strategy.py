import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'CCITurbo': 1.0
        })
    )
