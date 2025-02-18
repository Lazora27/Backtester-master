import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'FlowOfFunds': 1.0
        })
    )
