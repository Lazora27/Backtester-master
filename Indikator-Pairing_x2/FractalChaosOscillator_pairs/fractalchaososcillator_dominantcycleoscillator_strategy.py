import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
