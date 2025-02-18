import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
