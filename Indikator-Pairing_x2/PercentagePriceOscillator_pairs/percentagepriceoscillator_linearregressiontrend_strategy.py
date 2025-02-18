import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
