import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
