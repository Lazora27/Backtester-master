import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und OpenInterest
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'OpenInterest': 1.0
        })
    )
