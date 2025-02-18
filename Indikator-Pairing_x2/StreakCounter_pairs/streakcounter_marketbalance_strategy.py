import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketBalance': 1.0
        })
    )
