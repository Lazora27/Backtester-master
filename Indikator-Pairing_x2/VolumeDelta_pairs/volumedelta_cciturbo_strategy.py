import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'CCITurbo': 1.0
        })
    )
