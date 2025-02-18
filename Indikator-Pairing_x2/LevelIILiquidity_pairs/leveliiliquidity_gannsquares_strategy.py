import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und GannSquares
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'GannSquares': 1.0
        })
    )
