import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'WolfeWaves': 1.0
        })
    )
