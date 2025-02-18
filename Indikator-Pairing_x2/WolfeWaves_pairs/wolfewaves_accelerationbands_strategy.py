import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AccelerationBands': 1.0
        })
    )
