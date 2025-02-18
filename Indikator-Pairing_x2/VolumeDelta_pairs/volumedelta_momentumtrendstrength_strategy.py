import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
