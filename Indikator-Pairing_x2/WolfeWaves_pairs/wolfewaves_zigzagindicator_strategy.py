import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
