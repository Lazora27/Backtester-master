import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und COTReport
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'COTReport': 1.0
        })
    )
