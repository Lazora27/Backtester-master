import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'FibonacciZones': 1.0
        })
    )
