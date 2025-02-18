import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
