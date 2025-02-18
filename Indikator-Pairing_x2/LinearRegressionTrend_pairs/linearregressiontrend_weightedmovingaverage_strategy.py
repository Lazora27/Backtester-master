import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
