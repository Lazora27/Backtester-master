import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FibonacciZones': 1.0
        })
    )
