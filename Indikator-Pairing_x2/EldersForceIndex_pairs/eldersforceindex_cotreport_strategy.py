import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'COTReport': 1.0
        })
    )
