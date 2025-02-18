import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'DonchianVolatility': 1.0
        })
    )
