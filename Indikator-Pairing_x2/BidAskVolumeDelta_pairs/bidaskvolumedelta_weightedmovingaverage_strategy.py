import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
