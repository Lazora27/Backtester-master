import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
