import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AroonIndicator': 1.0
        })
    )
