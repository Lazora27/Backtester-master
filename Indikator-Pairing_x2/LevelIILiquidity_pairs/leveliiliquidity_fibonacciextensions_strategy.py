import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
