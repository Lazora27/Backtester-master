import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
