import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
