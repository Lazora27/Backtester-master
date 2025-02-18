import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
