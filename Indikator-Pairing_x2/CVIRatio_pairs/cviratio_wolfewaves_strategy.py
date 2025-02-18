import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WolfeWaves': 1.0
        })
    )
