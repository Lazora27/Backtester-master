import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
