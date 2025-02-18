import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
