import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
