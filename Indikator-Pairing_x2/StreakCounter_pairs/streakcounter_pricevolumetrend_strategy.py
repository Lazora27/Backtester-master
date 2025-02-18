import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
