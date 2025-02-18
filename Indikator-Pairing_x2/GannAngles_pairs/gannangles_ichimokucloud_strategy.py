import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'IchimokuCloud': 1.0
        })
    )
