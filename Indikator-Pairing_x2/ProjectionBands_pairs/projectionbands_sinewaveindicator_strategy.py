import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
