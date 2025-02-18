import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
