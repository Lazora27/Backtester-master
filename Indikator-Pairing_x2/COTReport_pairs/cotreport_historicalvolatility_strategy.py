import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
