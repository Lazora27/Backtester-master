import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
