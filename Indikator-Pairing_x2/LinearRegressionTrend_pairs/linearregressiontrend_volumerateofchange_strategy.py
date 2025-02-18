import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
