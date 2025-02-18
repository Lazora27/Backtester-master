import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
