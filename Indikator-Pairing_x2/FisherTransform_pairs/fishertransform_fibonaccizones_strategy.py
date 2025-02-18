import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FibonacciZones': 1.0
        })
    )
