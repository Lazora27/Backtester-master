import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TimeCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TimeCycle': 1.0
        })
    )
