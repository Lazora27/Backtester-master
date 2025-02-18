import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und CCITurbo
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'CCITurbo': 1.0
        })
    )
