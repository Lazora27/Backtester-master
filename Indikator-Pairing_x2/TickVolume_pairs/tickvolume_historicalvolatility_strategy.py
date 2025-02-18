import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
