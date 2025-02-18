import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
