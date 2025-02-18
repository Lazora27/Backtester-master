import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
