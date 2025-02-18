import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und COTReport
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'COTReport': 1.0
        })
    )
