import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'VolumeDelta': 1.0
        })
    )
