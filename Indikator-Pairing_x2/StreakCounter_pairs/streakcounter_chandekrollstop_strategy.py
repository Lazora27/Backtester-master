import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
