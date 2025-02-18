import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'OpenInterest': 1.0
        })
    )
