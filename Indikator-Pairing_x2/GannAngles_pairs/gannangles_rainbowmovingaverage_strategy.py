import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
