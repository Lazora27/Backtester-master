import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BollingerBands': 1.0
        })
    )
