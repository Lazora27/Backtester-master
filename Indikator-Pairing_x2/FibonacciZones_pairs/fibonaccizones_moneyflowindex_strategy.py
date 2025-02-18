import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
