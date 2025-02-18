import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
