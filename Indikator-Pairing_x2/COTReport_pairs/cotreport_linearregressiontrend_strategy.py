import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
