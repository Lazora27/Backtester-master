import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'FlowOfFunds': 1.0
        })
    )
