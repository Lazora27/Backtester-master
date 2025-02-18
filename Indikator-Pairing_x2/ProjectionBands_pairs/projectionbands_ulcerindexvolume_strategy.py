import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
