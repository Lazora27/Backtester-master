import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
