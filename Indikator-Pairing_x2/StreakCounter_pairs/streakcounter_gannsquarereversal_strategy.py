import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'GannSquareReversal': 1.0
        })
    )
