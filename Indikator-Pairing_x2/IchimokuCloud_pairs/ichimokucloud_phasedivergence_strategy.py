import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'PhaseDivergence': 1.0
        })
    )
