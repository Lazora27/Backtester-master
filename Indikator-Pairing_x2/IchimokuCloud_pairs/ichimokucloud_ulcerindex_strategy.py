import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'UlcerIndex': 1.0
        })
    )
