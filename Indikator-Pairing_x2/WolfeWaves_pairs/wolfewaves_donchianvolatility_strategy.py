import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DonchianVolatility': 1.0
        })
    )
