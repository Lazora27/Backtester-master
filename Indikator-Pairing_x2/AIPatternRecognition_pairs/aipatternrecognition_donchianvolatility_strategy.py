import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'DonchianVolatility': 1.0
        })
    )
