import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
