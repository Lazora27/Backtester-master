import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
