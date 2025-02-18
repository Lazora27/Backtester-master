import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VolatilityIndex': 1.0
        })
    )
