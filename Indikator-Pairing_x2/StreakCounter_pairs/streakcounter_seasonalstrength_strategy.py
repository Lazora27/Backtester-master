import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SeasonalStrength': 1.0
        })
    )
