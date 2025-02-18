import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und GannFans
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'GannFans': 1.0
        })
    )
