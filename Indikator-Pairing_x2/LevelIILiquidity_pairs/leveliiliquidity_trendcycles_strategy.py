import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TrendCycles
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TrendCycles': 1.0
        })
    )
