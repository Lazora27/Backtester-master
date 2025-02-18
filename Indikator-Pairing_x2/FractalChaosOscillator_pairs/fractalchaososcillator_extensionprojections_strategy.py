import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
