import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FibonacciZones': 1.0
        })
    )
