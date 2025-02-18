import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
