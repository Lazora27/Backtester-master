import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'DemandIndex': 1.0
        })
    )
