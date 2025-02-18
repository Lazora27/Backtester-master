import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AccelerationBands': 1.0
        })
    )
