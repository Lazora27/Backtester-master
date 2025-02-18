import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'DPOCycles': 1.0
        })
    )
