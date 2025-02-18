import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BarStrength
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BarStrength': 1.0
        })
    )
