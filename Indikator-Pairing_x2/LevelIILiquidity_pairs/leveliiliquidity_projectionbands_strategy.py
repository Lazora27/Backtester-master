import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ProjectionBands': 1.0
        })
    )
