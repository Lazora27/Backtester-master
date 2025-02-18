import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
