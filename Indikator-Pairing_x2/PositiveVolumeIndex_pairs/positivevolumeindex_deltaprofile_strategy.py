import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
