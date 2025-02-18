import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SinewaveOscillator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SinewaveOscillator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'SinewaveOscillator': {
                'class': SinewaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SinewaveOscillator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'SinewaveOscillator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
