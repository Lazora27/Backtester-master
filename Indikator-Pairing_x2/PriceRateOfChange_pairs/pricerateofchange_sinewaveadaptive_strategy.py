import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
