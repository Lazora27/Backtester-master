import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'PhaseDivergence': 1.0
        })
    )
