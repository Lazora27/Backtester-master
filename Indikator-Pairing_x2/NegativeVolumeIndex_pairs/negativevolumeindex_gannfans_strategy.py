import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'GannFans': 1.0
        })
    )
