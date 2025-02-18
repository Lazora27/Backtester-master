import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'PhaseDivergence': 1.0
        })
    )
