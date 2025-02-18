import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
