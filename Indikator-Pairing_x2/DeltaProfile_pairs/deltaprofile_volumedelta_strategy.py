import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeDelta': 1.0
        })
    )
