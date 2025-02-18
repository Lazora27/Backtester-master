import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
