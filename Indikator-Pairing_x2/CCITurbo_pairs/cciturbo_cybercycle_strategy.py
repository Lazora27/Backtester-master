import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'CyberCycle': 1.0
        })
    )
