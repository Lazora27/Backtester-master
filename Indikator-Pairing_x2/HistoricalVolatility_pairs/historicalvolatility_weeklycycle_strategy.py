import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'WeeklyCycle': 1.0
        })
    )
