import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
