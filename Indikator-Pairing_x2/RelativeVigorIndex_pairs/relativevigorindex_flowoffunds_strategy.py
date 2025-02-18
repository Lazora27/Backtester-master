import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
