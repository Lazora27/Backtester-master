import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'KeltnerChannels': 1.0
        })
    )
