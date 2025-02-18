import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
