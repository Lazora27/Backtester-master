import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TapeReading
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TapeReading': 1.0
        })
    )
