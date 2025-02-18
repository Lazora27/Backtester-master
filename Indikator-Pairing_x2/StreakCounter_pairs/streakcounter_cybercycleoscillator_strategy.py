import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
