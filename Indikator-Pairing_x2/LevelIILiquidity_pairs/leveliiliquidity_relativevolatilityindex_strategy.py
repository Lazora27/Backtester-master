import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_RelativeVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und RelativeVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'RelativeVolatilityIndex': 1.0
        })
    )
