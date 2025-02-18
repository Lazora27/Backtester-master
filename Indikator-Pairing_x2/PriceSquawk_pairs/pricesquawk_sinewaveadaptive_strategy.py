import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
