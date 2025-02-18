import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'WolfeWaves': 1.0
        })
    )
