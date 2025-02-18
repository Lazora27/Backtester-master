import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
