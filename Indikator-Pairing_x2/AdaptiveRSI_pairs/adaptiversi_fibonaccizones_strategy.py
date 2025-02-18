import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FibonacciZones': 1.0
        })
    )
