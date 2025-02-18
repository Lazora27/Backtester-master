import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
