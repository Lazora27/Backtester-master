import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'GannFans': 1.0
        })
    )
