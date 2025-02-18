import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
