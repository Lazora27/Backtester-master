import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersCenterOfGravityOscillator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersCenterOfGravityOscillator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'EhlersCenterOfGravityOscillator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
