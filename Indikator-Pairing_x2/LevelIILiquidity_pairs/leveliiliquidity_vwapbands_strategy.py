import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und VWAPBands
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'VWAPBands': 1.0
        })
    )
