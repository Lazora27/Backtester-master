import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'CCITurbo': 1.0
        })
    )
