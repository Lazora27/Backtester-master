import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
