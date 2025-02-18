import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_WyckoffWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und WyckoffWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'WyckoffWaveIndicator': 1.0
        })
    )
