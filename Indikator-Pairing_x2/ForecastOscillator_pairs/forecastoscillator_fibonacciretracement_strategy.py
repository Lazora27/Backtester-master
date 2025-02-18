import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
