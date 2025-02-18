import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
