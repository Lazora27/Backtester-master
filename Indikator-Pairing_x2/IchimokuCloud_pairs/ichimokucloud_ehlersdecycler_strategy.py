import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'EhlersDecycler': 1.0
        })
    )
