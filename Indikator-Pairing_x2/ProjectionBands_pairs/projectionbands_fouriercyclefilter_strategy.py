import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
