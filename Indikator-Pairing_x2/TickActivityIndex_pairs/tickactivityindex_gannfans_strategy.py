import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'GannFans': 1.0
        })
    )
