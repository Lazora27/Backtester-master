import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TrendCycles': 1.0
        })
    )
