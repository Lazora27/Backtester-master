import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
