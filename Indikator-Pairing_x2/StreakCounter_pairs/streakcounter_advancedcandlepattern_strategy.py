import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
