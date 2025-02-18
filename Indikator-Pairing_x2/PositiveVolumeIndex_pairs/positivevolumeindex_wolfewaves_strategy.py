import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
