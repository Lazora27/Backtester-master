import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'AdaptiveATR': 1.0
        })
    )
