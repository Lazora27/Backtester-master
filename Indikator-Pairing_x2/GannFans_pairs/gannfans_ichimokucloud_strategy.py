import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'IchimokuCloud': 1.0
        })
    )
