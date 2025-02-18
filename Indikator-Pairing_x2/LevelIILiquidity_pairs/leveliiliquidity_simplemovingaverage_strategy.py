import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
