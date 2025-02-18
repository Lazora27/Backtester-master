import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
