import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
