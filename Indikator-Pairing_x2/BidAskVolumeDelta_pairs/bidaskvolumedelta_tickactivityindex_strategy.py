import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'TickActivityIndex': 1.0
        })
    )
