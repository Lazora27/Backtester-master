import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'COTReport': 1.0
        })
    )
