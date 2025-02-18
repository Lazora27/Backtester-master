import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CyberCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CyberCycle': 1.0
        })
    )
