import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'MassIndex': 1.0
        })
    )
