import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DeltaProfile': 1.0
        })
    )
