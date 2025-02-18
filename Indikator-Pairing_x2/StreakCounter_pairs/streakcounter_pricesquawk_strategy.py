import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PriceSquawk': 1.0
        })
    )
