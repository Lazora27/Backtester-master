import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'GannSquareReversal': 1.0
        })
    )
