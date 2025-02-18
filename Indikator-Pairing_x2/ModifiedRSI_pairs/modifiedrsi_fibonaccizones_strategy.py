import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FibonacciZones': 1.0
        })
    )
