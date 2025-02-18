import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
