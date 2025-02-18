import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'Fisher': 1.0
        })
    )
