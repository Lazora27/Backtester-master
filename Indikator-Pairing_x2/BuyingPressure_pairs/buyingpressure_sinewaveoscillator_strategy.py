import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
