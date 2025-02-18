import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MACDPredictor': 1.0
        })
    )
