import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'VolumeOscillator': 1.0
        })
    )
