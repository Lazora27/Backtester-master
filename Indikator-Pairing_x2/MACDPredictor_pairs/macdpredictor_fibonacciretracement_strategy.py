import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
