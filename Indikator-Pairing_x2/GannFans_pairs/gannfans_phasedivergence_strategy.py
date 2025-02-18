import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'PhaseDivergence': 1.0
        })
    )
