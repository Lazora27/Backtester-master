import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und DemandIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'DemandIndex': 1.0
        })
    )
