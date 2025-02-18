import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
