import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'FlowOfFunds': 1.0
        })
    )
