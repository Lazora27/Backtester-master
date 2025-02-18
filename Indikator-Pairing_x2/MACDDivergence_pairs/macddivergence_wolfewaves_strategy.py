import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WolfeWaves': 1.0
        })
    )
