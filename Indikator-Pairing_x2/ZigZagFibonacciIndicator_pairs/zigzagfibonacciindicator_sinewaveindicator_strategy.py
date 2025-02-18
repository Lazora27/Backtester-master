import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagFibonacciIndicator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagFibonacciIndicator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ZigZagFibonacciIndicator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
