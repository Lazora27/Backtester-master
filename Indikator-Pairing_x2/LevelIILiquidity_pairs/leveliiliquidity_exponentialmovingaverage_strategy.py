import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
