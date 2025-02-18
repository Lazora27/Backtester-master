import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
