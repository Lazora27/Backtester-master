import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AverageTrueRange': 1.0
        })
    )
