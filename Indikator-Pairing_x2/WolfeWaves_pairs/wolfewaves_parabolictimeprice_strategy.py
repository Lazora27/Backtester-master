import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
