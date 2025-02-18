import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
