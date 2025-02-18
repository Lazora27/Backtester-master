import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
