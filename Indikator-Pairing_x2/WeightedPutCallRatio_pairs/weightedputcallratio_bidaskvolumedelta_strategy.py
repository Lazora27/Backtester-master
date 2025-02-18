import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
