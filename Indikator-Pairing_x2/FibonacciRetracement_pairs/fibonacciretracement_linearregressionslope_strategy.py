import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
