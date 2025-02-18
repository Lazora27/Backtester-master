import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
