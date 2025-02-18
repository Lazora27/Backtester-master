import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
