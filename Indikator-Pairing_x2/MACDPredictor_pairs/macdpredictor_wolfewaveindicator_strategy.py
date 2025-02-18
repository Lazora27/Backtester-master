import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
