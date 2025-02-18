import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
