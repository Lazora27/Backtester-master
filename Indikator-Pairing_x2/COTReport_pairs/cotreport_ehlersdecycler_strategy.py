import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'EhlersDecycler': 1.0
        })
    )
