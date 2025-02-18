import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und MassIndex
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'MassIndex': 1.0
        })
    )
