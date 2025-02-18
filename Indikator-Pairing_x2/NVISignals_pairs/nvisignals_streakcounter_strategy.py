import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StreakCounter
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StreakCounter': 1.0
        })
    )
