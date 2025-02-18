import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'WolfeWaves': 1.0
        })
    )
