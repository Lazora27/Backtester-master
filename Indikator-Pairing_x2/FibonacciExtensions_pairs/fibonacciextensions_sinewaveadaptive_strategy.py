import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
