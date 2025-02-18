import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FibonacciZones': 1.0
        })
    )
