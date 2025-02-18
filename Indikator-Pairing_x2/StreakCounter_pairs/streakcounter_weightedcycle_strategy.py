import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'WeightedCycle': 1.0
        })
    )
