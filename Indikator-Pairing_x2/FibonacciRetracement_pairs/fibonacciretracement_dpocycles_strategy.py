import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'DPOCycles': 1.0
        })
    )
