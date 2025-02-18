import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
