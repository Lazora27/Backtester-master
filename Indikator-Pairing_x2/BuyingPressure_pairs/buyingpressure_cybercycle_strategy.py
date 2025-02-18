import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'CyberCycle': 1.0
        })
    )
