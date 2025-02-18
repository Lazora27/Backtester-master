import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'PhaseDivergence': 1.0
        })
    )
