import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und COTReport
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'COTReport': 1.0
        })
    )
