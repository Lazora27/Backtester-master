import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
