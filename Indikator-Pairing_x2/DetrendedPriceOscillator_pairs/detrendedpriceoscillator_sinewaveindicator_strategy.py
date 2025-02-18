import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DetrendedPriceOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
