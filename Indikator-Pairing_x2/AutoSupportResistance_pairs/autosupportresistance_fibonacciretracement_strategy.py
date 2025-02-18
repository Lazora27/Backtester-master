import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
