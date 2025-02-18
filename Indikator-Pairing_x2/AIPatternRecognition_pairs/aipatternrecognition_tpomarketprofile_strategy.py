import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
