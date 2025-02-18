import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
