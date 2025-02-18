import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
