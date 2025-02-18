import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
