import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PhaseDivergence': 1.0
        })
    )
