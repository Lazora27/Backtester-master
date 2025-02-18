import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
