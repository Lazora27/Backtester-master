import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
