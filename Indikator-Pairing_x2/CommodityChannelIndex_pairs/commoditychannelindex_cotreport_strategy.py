import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'COTReport': 1.0
        })
    )
