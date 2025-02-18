import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WolfeWaves': 1.0
        })
    )
