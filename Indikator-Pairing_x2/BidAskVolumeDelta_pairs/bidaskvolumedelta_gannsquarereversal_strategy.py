import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'GannSquareReversal': 1.0
        })
    )
