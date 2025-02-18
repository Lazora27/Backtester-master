import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
