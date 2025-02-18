import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MassIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MassIndex': 1.0
        })
    )
