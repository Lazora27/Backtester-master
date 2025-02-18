import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WolfeWaves': 1.0
        })
    )
