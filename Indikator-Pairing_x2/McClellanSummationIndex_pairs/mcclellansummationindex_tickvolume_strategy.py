import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TickVolume
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TickVolume': 1.0
        })
    )
