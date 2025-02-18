import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und MovingAverage
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'MovingAverage': 1.0
        })
    )
