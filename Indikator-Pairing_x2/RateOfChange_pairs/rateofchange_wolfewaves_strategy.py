import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WolfeWaves': 1.0
        })
    )
