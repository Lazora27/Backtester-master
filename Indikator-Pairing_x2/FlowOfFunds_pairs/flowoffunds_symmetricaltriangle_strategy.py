import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
