import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
