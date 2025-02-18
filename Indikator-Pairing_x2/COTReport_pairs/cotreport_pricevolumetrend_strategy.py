import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
