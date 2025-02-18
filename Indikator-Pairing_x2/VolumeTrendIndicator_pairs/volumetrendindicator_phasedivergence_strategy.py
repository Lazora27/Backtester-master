import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
