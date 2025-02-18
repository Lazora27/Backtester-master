import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BollingerBands': 1.0
        })
    )
