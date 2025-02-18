import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
