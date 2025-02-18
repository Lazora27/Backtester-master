import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'CyberCycle': 1.0
        })
    )
