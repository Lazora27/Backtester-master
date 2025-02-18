import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
