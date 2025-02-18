import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
