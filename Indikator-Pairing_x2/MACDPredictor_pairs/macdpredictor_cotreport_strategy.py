import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und COTReport
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'COTReport': 1.0
        })
    )
