import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'CyberCycle': 1.0
        })
    )
