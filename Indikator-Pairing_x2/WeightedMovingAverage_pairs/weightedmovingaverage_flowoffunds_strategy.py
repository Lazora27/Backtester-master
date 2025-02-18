import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'FlowOfFunds': 1.0
        })
    )
