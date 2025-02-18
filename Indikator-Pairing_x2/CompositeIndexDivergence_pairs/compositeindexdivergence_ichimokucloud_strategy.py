import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'IchimokuCloud': 1.0
        })
    )
