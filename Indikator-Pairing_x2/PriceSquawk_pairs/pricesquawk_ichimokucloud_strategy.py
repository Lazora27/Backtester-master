import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'IchimokuCloud': 1.0
        })
    )
