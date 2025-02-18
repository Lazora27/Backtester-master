import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und COTReport
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'COTReport': 1.0
        })
    )
