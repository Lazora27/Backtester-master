import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'TimeCycle': 1.0
        })
    )
