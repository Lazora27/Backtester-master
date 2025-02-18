import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BuyingPressure': 1.0
        })
    )
