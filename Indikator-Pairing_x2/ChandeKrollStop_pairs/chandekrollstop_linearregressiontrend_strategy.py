import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
