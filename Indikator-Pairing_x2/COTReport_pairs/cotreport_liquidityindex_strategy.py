import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'LiquidityIndex': 1.0
        })
    )
