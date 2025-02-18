import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
