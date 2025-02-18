import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
