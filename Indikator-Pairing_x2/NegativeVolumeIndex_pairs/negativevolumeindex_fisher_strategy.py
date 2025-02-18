import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'Fisher': 1.0
        })
    )
