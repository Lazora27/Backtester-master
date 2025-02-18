import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'HullMovingAverage': 1.0
        })
    )
