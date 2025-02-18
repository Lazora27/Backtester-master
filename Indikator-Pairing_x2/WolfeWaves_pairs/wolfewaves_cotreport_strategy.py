import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und COTReport
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'COTReport': 1.0
        })
    )
