import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
