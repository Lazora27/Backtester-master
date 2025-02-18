import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SeasonalStrength': 1.0
        })
    )
