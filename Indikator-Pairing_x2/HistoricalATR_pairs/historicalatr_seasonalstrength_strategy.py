import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SeasonalStrength': 1.0
        })
    )
