import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und DPOCycles
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'DPOCycles': 1.0
        })
    )
