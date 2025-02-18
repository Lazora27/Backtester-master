import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FlowOfFunds': 1.0
        })
    )
