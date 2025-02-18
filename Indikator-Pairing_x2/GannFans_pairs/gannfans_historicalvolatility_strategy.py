import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
