import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und FisherSignals
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'FisherSignals': 1.0
        })
    )
