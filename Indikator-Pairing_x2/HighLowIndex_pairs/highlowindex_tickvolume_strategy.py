import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TickVolume
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TickVolume': 1.0
        })
    )
