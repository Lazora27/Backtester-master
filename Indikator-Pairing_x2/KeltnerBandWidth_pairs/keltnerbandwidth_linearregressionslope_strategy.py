import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
