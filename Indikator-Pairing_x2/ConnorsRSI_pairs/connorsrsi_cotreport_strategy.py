import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'COTReport': 1.0
        })
    )
