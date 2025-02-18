import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
