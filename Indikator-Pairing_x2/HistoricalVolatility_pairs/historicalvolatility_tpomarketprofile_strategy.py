import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
