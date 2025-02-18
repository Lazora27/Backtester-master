import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PhaseDivergence': 1.0
        })
    )
