import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'FlowOfFunds': 1.0
        })
    )
