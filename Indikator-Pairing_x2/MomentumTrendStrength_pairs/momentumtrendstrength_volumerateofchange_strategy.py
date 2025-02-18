import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
