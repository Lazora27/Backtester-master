import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'WolfeWaves': 1.0
        })
    )
