import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
