import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und FisherSignals
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'FisherSignals': 1.0
        })
    )
