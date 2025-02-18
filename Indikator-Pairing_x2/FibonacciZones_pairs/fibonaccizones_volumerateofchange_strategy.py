import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
