import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
