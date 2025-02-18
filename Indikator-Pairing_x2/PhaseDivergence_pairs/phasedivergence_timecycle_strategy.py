import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'TimeCycle': 1.0
        })
    )
