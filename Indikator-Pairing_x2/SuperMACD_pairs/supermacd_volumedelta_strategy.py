import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VolumeDelta': 1.0
        })
    )
