import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CyberCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CyberCycle': 1.0
        })
    )
