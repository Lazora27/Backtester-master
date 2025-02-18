import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BollingerPercentB': 1.0
        })
    )
