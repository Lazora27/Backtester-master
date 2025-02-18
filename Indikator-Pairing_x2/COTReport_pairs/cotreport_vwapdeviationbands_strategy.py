import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
