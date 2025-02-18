import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VWAPBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VWAPBands': 1.0
        })
    )
