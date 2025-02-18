import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
