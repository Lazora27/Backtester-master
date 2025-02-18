import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
