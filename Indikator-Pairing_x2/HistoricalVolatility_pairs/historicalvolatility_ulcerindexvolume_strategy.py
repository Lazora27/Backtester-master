import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
