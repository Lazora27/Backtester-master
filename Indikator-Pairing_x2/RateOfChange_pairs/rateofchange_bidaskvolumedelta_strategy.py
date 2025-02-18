import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
