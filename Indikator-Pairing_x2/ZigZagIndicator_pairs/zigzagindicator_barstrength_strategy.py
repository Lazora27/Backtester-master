import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
