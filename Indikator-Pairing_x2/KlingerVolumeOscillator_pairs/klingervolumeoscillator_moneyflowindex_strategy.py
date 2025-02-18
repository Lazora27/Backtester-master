import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KlingerVolumeOscillator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KlingerVolumeOscillator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'KlingerVolumeOscillator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
