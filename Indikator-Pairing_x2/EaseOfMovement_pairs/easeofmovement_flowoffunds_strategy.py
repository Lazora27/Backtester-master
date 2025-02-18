import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'FlowOfFunds': 1.0
        })
    )
