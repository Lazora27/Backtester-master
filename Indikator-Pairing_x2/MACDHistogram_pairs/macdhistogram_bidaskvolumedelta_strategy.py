import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
