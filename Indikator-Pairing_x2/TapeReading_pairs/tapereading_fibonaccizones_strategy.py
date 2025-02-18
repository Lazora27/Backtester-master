import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FibonacciZones': 1.0
        })
    )
