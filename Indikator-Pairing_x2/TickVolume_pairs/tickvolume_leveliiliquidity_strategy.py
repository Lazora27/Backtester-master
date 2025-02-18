import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
