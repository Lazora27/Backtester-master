import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
