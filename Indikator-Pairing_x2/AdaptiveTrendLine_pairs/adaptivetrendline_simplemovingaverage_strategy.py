import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
