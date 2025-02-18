import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
