import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'PhaseDivergence': 1.0
        })
    )
