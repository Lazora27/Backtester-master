import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
