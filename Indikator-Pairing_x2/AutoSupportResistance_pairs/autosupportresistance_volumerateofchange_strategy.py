import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
