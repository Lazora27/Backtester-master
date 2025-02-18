import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
