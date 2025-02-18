import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SymmetricalTriangle_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SymmetricalTriangle und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SymmetricalTriangle': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
