import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
