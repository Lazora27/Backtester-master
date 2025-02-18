import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und MassIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'MassIndex': 1.0
        })
    )
