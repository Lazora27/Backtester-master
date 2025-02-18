import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
