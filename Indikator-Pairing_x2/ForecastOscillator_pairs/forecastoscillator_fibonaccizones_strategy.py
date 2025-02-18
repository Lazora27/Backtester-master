import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
