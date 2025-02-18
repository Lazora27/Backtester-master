import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'BradleySiderograph': 1.0
        })
    )
