import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
