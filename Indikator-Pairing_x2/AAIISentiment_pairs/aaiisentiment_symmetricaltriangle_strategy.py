import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
