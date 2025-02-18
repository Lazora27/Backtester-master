import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CycleFinder': 1.0
        })
    )
