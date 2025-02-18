import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'LiquidityIndex': 1.0
        })
    )
