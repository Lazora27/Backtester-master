import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SeasonalStrength': 1.0
        })
    )
