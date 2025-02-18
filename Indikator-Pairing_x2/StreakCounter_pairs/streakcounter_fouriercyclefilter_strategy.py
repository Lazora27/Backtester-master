import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
