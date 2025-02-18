import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
