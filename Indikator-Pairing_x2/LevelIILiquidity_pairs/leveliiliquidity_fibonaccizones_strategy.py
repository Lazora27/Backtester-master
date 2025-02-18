import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FibonacciZones': 1.0
        })
    )
