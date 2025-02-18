import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
