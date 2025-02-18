import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
