import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'EaseOfMovement': 1.0
        })
    )
