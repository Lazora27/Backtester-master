import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SeasonalStrength': 1.0
        })
    )
