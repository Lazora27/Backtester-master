import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
