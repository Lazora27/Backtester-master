import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SinewaveOscillator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SinewaveOscillator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SinewaveOscillator': {
                'class': SinewaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SinewaveOscillator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SinewaveOscillator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
