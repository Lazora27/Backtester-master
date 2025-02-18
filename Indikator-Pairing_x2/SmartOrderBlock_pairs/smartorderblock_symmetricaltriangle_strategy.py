import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
