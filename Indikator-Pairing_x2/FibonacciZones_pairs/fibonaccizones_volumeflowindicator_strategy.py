import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
