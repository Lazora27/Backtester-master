import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ParabolicSAR': 1.0
        })
    )
