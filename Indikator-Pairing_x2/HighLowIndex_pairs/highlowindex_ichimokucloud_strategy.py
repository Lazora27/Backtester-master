import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
