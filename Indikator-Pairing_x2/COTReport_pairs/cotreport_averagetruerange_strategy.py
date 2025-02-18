import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AverageTrueRange': 1.0
        })
    )
