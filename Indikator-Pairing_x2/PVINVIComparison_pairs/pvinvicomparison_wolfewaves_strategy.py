import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WolfeWaves': 1.0
        })
    )
