import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'IntradayIntensity': 1.0
        })
    )
