import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
