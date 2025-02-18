import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'DeltaProfile': 1.0
        })
    )
