import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BuyingPressure': 1.0
        })
    )
