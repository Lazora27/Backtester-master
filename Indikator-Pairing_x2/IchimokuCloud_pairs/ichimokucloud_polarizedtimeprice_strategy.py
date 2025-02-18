import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
