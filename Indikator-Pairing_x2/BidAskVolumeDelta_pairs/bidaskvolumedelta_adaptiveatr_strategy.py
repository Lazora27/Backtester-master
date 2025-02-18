import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'AdaptiveATR': 1.0
        })
    )
