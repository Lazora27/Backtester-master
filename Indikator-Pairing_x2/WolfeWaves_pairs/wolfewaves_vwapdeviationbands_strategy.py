import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
