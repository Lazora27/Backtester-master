import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
