import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
