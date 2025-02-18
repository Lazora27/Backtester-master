import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
