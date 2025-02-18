import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'WolfeWaves': 1.0
        })
    )
