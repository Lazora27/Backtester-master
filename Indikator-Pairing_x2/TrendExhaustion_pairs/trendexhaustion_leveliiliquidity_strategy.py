import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
