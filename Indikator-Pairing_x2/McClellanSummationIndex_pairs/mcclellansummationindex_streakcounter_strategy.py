import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
