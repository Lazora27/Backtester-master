import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
