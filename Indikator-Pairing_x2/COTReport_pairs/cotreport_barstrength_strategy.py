import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BarStrength
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BarStrength': 1.0
        })
    )
