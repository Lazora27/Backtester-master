import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
