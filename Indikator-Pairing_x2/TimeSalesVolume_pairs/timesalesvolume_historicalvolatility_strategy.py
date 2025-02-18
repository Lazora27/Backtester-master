import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
