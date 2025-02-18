import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
