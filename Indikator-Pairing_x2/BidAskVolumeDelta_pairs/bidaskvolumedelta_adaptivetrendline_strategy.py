import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
