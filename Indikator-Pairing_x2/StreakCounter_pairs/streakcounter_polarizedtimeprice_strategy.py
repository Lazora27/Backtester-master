import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
