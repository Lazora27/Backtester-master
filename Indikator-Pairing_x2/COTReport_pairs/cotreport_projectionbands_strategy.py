import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ProjectionBands': 1.0
        })
    )
