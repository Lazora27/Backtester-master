import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
