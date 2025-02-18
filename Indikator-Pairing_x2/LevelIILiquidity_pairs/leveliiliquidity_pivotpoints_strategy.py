import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PivotPoints
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PivotPoints': 1.0
        })
    )
