import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
