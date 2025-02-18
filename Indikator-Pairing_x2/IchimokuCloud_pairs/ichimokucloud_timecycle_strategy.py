import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TimeCycle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TimeCycle': 1.0
        })
    )
