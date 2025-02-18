import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'TimeCycle': 1.0
        })
    )
