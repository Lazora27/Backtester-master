import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
