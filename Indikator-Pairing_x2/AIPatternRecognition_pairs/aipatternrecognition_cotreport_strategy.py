import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und COTReport
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'COTReport': 1.0
        })
    )
