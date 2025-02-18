import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
