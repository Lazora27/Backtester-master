import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
