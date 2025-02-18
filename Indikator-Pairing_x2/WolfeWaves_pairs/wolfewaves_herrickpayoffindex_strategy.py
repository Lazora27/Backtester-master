import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
