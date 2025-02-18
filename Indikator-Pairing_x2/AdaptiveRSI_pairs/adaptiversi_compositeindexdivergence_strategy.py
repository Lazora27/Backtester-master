import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
