import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und COTReport
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'COTReport': 1.0
        })
    )
