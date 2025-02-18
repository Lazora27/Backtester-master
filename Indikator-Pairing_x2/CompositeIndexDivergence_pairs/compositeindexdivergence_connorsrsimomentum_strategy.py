import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_ConnorsRSIMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und ConnorsRSIMomentum
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'ConnorsRSIMomentum': 1.0
        })
    )
