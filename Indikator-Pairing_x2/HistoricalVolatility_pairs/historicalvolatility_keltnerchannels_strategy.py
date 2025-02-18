import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'KeltnerChannels': 1.0
        })
    )
