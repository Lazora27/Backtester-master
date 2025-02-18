import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PhaseDivergence': 1.0
        })
    )
