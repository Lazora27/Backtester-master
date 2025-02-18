import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und GannAngles
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'GannAngles': 1.0
        })
    )
