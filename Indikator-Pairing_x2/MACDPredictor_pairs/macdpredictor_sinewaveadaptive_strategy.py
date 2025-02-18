import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
