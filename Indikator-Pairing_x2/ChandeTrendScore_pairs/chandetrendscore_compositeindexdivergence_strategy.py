import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
