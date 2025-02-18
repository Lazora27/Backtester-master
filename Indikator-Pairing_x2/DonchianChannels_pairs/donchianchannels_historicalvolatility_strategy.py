import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
