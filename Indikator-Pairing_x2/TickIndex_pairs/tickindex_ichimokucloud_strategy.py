import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
