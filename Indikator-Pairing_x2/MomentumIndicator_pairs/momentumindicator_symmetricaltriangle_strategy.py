import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
