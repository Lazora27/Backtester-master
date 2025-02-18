import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SmartMoneyConceptsIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SmartMoneyConceptsIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SmartMoneyConceptsIndicator': 1.0
        })
    )
