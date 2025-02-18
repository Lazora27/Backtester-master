import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
