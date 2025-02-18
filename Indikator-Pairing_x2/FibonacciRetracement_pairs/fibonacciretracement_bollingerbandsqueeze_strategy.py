import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
