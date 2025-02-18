import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
