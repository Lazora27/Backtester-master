import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
