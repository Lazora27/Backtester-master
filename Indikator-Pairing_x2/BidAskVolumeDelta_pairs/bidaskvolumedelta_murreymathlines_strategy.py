import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'MurreyMathLines': 1.0
        })
    )
