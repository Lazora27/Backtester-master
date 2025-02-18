import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'WolfeWaves': 1.0
        })
    )
