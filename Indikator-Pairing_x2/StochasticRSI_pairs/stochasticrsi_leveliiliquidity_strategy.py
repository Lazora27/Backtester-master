import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
