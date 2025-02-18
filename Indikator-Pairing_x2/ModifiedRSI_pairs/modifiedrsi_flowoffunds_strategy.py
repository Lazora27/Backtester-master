import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FlowOfFunds': 1.0
        })
    )
