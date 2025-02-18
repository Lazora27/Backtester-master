import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
