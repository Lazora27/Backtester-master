import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SeasonalStrength': 1.0
        })
    )
