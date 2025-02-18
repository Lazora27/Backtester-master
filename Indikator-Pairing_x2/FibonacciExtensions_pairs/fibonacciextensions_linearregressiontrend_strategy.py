import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
