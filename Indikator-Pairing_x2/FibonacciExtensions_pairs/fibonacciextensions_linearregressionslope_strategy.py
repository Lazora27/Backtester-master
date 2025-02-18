import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
