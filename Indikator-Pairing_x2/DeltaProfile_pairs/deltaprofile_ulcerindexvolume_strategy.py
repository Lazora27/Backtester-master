import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
