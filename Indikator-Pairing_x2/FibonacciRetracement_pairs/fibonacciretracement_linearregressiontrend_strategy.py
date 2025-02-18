import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
