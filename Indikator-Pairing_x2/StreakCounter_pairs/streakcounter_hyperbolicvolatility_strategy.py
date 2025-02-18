import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
