import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'WolfeWaves': 1.0
        })
    )
