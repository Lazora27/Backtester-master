import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsAccumulationDistribution_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsAccumulationDistribution und COTReport
    """
    
    params = (
        ('indicators', {
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'WilliamsAccumulationDistribution': 1.0,
            'COTReport': 1.0
        })
    )
