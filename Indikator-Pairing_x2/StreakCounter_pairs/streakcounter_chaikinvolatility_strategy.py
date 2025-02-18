import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
