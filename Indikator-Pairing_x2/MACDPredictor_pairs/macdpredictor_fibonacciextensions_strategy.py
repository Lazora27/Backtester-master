import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
