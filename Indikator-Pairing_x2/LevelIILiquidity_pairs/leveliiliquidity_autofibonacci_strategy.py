import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AutoFibonacci': 1.0
        })
    )
