import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
