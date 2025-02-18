import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
