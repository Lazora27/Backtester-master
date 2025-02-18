import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
