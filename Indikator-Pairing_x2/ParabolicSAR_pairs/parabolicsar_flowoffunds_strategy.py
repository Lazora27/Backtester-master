import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'FlowOfFunds': 1.0
        })
    )
