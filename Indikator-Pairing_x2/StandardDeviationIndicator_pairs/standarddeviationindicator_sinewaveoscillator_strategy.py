import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
