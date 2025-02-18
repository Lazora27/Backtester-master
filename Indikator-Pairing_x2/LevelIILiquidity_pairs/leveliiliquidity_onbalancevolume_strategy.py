import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
