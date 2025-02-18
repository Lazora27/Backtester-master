import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
