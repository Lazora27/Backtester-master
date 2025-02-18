import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
