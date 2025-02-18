import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
