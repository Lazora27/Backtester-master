import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
