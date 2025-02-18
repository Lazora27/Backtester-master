import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und MassIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'MassIndex': 1.0
        })
    )
