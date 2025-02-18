import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
