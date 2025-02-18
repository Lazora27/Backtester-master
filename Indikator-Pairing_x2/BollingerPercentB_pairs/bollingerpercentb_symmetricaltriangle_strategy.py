import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
