import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und GannSquares
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'GannSquares': 1.0
        })
    )
