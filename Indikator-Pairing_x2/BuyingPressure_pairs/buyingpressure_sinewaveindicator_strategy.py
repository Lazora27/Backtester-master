import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
