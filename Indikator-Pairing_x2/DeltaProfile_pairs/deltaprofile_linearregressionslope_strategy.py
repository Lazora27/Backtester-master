import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
