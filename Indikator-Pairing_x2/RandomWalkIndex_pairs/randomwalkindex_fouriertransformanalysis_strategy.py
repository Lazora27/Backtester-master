import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
