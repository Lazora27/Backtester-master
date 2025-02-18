import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
