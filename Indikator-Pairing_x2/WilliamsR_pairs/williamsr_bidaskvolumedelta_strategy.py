import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
