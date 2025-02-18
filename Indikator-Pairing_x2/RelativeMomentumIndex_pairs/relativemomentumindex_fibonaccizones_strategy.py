import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
