import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
