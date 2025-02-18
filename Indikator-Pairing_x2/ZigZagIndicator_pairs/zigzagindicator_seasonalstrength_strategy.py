import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
