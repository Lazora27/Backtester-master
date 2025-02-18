import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AccelerationBands': 1.0
        })
    )
