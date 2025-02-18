import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedVolatilityIndex_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedVolatilityIndex und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'NormalizedVolatilityIndex': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
