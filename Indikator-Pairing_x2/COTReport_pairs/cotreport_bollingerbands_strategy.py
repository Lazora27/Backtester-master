import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BollingerBands
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BollingerBands': 1.0
        })
    )
