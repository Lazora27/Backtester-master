import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
