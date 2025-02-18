import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
