import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
