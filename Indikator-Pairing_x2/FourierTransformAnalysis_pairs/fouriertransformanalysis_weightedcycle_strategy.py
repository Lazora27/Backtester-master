import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'WeightedCycle': 1.0
        })
    )
