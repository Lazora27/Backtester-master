import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'FlowOfFunds': 1.0
        })
    )
