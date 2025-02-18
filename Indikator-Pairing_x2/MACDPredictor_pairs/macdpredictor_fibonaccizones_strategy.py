import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FibonacciZones': 1.0
        })
    )
