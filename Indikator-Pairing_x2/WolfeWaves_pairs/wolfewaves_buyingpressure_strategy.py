import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BuyingPressure': 1.0
        })
    )
