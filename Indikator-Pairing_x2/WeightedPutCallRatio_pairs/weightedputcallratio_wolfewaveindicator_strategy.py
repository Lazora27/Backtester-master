import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
