import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
