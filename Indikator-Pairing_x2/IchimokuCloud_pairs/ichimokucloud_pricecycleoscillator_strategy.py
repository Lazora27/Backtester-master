import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
