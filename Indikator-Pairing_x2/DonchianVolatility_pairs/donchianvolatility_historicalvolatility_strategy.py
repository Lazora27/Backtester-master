import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
