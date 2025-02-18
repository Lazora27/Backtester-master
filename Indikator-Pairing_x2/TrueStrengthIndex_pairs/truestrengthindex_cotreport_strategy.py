import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'COTReport': 1.0
        })
    )
