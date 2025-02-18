import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'BollingerPercentB': 1.0
        })
    )
