import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und DPOCycles
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'DPOCycles': 1.0
        })
    )
