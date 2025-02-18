import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
