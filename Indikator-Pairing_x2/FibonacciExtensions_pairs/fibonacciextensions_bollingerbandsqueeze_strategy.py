import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
