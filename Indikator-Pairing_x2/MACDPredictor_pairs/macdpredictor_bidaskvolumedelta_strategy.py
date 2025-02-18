import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
