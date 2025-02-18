import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
