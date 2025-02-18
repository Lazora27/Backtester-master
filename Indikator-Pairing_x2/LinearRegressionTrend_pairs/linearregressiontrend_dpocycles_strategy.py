import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und DPOCycles
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'DPOCycles': 1.0
        })
    )
