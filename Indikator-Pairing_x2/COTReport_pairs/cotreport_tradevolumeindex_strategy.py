import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
