import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BollingerBands
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BollingerBands': 1.0
        })
    )
