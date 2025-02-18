import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PriceDelta
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PriceDelta': 1.0
        })
    )
