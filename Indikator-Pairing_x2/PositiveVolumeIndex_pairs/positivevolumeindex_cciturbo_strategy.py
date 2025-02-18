import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
