import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
