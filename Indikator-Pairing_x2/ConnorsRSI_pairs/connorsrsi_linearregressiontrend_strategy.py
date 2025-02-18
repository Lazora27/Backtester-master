import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
