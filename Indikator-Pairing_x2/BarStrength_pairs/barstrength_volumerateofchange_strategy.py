import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
