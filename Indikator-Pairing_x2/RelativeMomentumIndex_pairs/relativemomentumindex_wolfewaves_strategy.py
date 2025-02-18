import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
