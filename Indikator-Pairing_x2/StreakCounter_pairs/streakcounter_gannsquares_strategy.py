import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und GannSquares
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'GannSquares': 1.0
        })
    )
