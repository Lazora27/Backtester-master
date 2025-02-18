import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
