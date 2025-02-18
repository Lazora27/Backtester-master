import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
