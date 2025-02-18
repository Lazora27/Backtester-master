import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'BradleySiderograph': 1.0
        })
    )
