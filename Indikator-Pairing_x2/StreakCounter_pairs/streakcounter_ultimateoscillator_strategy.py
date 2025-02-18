import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'UltimateOscillator': 1.0
        })
    )
