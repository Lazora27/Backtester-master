import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SmoothedCycle': 1.0
        })
    )
