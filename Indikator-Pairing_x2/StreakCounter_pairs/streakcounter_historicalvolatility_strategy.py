import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
