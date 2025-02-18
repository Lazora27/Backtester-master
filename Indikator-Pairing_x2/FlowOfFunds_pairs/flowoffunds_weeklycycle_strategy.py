import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'WeeklyCycle': 1.0
        })
    )
