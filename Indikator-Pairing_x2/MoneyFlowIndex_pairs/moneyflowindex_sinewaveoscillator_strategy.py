import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
