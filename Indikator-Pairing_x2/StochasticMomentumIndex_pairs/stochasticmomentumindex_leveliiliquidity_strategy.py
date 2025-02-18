import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
