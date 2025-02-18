import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
