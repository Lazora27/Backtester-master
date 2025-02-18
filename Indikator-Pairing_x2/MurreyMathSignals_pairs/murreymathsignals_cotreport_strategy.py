import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und COTReport
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'COTReport': 1.0
        })
    )
