import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
