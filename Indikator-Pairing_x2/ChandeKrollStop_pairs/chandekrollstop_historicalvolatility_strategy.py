import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
