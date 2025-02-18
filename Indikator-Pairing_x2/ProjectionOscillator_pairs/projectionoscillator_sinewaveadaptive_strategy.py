import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
