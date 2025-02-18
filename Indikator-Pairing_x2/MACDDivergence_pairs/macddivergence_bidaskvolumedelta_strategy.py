import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
