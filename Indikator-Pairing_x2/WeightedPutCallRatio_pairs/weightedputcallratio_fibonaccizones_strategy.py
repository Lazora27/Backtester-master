import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'FibonacciZones': 1.0
        })
    )
