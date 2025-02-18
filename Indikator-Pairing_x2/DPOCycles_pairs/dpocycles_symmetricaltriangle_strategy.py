import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
