import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AverageLogRange': 1.0
        })
    )
