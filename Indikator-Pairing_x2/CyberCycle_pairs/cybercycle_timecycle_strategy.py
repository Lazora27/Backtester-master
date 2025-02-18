import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'TimeCycle': 1.0
        })
    )
