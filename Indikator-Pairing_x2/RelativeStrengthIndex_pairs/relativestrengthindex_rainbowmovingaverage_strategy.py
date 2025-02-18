import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
