import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
