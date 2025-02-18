import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'GannFans': 1.0
        })
    )
