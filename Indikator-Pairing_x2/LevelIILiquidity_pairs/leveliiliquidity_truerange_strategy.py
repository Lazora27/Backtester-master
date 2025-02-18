import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TrueRange
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TrueRange': 1.0
        })
    )
