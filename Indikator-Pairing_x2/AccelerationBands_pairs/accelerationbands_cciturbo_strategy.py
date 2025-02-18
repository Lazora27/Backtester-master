import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'CCITurbo': 1.0
        })
    )
