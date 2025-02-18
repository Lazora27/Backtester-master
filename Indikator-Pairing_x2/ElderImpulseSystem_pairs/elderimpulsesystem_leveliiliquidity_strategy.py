import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
