import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'COTReport': 1.0
        })
    )
