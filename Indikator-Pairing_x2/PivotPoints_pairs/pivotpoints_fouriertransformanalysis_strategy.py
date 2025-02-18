import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
