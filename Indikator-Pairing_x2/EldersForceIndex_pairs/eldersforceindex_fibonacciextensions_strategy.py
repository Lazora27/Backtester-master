import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
