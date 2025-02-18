import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
