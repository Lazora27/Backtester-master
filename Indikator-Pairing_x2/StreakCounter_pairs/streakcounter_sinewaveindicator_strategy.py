import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
