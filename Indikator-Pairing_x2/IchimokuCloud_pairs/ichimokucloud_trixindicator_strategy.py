import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TRIXIndicator': 1.0
        })
    )
