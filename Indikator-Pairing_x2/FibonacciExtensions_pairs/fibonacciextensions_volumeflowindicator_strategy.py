import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
