import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
