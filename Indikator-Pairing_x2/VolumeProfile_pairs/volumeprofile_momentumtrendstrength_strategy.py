import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
