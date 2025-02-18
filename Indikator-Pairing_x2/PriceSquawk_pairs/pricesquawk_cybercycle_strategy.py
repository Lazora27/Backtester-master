import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CyberCycle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CyberCycle': 1.0
        })
    )
