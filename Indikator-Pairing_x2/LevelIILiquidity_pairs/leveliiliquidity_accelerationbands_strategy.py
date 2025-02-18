import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AccelerationBands': 1.0
        })
    )
