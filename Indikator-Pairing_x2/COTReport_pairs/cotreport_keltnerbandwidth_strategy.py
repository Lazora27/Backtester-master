import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
