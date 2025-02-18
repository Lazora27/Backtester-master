import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
