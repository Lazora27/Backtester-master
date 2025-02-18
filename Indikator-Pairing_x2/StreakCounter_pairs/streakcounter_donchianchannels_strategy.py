import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DonchianChannels': 1.0
        })
    )
