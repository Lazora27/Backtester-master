import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TrueRange
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TrueRange': 1.0
        })
    )
