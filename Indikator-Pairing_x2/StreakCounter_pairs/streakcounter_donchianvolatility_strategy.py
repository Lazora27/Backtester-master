import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DonchianVolatility': 1.0
        })
    )
