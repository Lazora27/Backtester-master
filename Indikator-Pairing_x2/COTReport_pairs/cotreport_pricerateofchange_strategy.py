import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
