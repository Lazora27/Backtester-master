import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
