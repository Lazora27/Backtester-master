import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
