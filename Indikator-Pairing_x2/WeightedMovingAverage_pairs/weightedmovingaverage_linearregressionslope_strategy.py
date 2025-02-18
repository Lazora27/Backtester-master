import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
