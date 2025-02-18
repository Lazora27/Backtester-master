import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'CumulativeTick': 1.0
        })
    )
