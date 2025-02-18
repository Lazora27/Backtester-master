import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
