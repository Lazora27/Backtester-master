import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'FlowOfFunds': 1.0
        })
    )
