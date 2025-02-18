import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
