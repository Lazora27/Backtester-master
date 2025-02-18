import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
