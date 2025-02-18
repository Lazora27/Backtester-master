import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
