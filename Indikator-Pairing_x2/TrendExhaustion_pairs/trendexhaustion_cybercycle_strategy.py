import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CyberCycle': 1.0
        })
    )
