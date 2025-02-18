import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und GannAngles
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'GannAngles': 1.0
        })
    )
