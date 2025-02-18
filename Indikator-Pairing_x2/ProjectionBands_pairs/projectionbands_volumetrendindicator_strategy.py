import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
