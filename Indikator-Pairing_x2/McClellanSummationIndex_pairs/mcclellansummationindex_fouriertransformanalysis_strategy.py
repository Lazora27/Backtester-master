import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
