import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_ArmsEaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und ArmsEaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'ArmsEaseOfMovement': 1.0
        })
    )
