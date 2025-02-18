import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'CCITurbo': 1.0
        })
    )
