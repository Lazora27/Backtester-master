import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und GannFans
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'GannFans': 1.0
        })
    )
