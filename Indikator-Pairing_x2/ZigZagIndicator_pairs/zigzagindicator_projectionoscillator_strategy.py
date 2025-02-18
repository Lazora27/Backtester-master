import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
