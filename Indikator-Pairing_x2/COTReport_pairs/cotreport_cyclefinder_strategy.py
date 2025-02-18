import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und CycleFinder
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'CycleFinder': 1.0
        })
    )
