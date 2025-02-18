import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und GannAngles
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'GannAngles': 1.0
        })
    )
