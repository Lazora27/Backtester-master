import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und COTReport
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'COTReport': 1.0
        })
    )
