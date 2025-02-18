import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
