import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'UltimateOscillator': 1.0
        })
    )
