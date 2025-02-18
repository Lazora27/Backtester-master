import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'UlcerIndex': 1.0
        })
    )
