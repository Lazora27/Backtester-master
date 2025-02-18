import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HistoricalATR': 1.0
        })
    )
